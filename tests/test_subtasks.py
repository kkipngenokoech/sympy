import pytest
from src.core.task_manager import TaskManager
from src.core.models import Task, TaskStatus, TaskPriority


class TestSubtasks:
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.task_manager = TaskManager()
    
    def test_add_subtask_success(self):
        """Test successfully adding a subtask to a parent task."""
        # Create parent and child tasks
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        # Add subtask relationship
        result = self.task_manager.add_subtask(parent.id, child.id)
        
        assert result is True
        assert child.id in parent.subtasks
        assert child.parent_task_id == parent.id
    
    def test_add_subtask_nonexistent_parent(self):
        """Test adding subtask with non-existent parent task."""
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        result = self.task_manager.add_subtask("nonexistent", child.id)
        
        assert result is False
        assert child.parent_task_id is None
    
    def test_add_subtask_nonexistent_child(self):
        """Test adding non-existent subtask to parent task."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        
        result = self.task_manager.add_subtask(parent.id, "nonexistent")
        
        assert result is False
        assert len(parent.subtasks) == 0
    
    def test_add_duplicate_subtask(self):
        """Test adding the same subtask twice to a parent."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        # Add subtask twice
        self.task_manager.add_subtask(parent.id, child.id)
        self.task_manager.add_subtask(parent.id, child.id)
        
        # Should only appear once in subtasks list
        assert parent.subtasks.count(child.id) == 1
        assert child.parent_task_id == parent.id
    
    def test_remove_subtask_success(self):
        """Test successfully removing a subtask from parent."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        # Add then remove subtask
        self.task_manager.add_subtask(parent.id, child.id)
        result = self.task_manager.remove_subtask(parent.id, child.id)
        
        assert result is True
        assert child.id not in parent.subtasks
        assert child.parent_task_id is None
    
    def test_remove_subtask_nonexistent_parent(self):
        """Test removing subtask from non-existent parent."""
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        result = self.task_manager.remove_subtask("nonexistent", child.id)
        
        assert result is False
    
    def test_remove_subtask_nonexistent_child(self):
        """Test removing non-existent subtask from parent."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        
        result = self.task_manager.remove_subtask(parent.id, "nonexistent")
        
        assert result is False
    
    def test_remove_subtask_not_in_parent(self):
        """Test removing subtask that's not in parent's subtask list."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child = self.task_manager.create_task("Child Task", "Subtask")
        
        # Don't add as subtask, just try to remove
        result = self.task_manager.remove_subtask(parent.id, child.id)
        
        assert result is True  # Operation succeeds even if not in list
        assert child.parent_task_id is None
    
    def test_get_subtasks_success(self):
        """Test retrieving subtasks of a parent task."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child1 = self.task_manager.create_task("Child 1", "First subtask")
        child2 = self.task_manager.create_task("Child 2", "Second subtask")
        
        # Add subtasks
        self.task_manager.add_subtask(parent.id, child1.id)
        self.task_manager.add_subtask(parent.id, child2.id)
        
        subtasks = self.task_manager.get_subtasks(parent.id)
        
        assert len(subtasks) == 2
        subtask_ids = [task.id for task in subtasks]
        assert child1.id in subtask_ids
        assert child2.id in subtask_ids
    
    def test_get_subtasks_nonexistent_parent(self):
        """Test retrieving subtasks of non-existent parent."""
        subtasks = self.task_manager.get_subtasks("nonexistent")
        
        assert subtasks == []
    
    def test_get_subtasks_no_subtasks(self):
        """Test retrieving subtasks when parent has none."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        
        subtasks = self.task_manager.get_subtasks(parent.id)
        
        assert subtasks == []
    
    def test_get_subtasks_with_deleted_subtask(self):
        """Test retrieving subtasks when one subtask has been deleted."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child1 = self.task_manager.create_task("Child 1", "First subtask")
        child2 = self.task_manager.create_task("Child 2", "Second subtask")
        
        # Add subtasks
        self.task_manager.add_subtask(parent.id, child1.id)
        self.task_manager.add_subtask(parent.id, child2.id)
        
        # Delete one subtask
        self.task_manager.delete_task(child1.id)
        
        subtasks = self.task_manager.get_subtasks(parent.id)
        
        # Should only return existing subtasks
        assert len(subtasks) == 1
        assert subtasks[0].id == child2.id
    
    def test_subtask_hierarchy_integrity(self):
        """Test that subtask relationships maintain integrity."""
        parent = self.task_manager.create_task("Parent Task", "Main task")
        child = self.task_manager.create_task("Child Task", "Subtask")
        grandchild = self.task_manager.create_task("Grandchild Task", "Sub-subtask")
        
        # Create hierarchy: parent -> child -> grandchild
        self.task_manager.add_subtask(parent.id, child.id)
        self.task_manager.add_subtask(child.id, grandchild.id)
        
        # Verify relationships
        assert child.id in parent.subtasks
        assert child.parent_task_id == parent.id
        assert grandchild.id in child.subtasks
        assert grandchild.parent_task_id == child.id
        
        # Verify subtask retrieval
        parent_subtasks = self.task_manager.get_subtasks(parent.id)
        child_subtasks = self.task_manager.get_subtasks(child.id)
        
        assert len(parent_subtasks) == 1
        assert parent_subtasks[0].id == child.id
        assert len(child_subtasks) == 1
        assert child_subtasks[0].id == grandchild.id
