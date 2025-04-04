from django.test import TestCase
from sproutapp.models import Subject, Content, Activity
from unittest.mock import patch, MagicMock

class SubjectModelTest(TestCase):

    def setUp(self):
        """Set up test data before each test."""
        # Mock CloudinaryField for testing
        self.subject = Subject.objects.create(
            subject_name="Mathematics",
            subject_image="mathematics.jpg",  # Just use string for testing
            subject_desc="Learn mathematics concepts and skills"
        )

    def test_subject_creation(self):
        """Test if a Subject instance is created correctly."""
        self.assertEqual(self.subject.subject_name, "Mathematics")
        self.assertEqual(str(self.subject.subject_image), "mathematics.jpg")
        self.assertEqual(self.subject.subject_desc, "Learn mathematics concepts and skills")

    def test_subject_str_method(self):
        """Test the __str__ method of Subject model."""
        self.assertEqual(str(self.subject), "Mathematics")

    def test_subject_auto_id(self):
        """Test if subject_id is auto-generated."""
        self.assertIsNotNone(self.subject.subject_id)

    def test_created_at_field(self):
        """Test if created_at is automatically set."""
        self.assertIsNotNone(self.subject.created_at)
    
    def test_field_max_lengths(self):
        """Test max length constraints of fields."""
        subject = Subject._meta.get_field('subject_name')
        self.assertEqual(subject.max_length, 100)
        desc = Subject._meta.get_field('subject_desc')
        self.assertEqual(desc.max_length, 255)


class ContentModelTest(TestCase):

    def setUp(self):
        """Set up test data before each test."""
        # Create a subject first
        self.subject = Subject.objects.create(
            subject_name="Science",
            subject_image="science.jpg",
            subject_desc="Explore scientific concepts and experiments"
        )

        # Create a content associated with the subject
        self.content = Content.objects.create(
            subject=self.subject,
            content_title="Physics",
            content_desc="Learn about forces and motion",
            content_icon="physics.svg"
        )

    def test_content_creation(self):
        """Test if a Content instance is created correctly."""
        self.assertEqual(self.content.content_title, "Physics")
        self.assertEqual(self.content.content_desc, "Learn about forces and motion")
        self.assertEqual(str(self.content.content_icon), "physics.svg")

    def test_content_str_method(self):
        """Test the __str__ method of Content model."""
        self.assertEqual(str(self.content), "Physics")

    def test_content_auto_id(self):
        """Test if content_id is auto-generated."""
        self.assertIsNotNone(self.content.content_id)

    def test_created_at_field(self):
        """Test if created_at is automatically set."""
        self.assertIsNotNone(self.content.created_at)

    def test_foreign_key_relation(self):
        """Test if the ForeignKey is correctly assigned."""
        self.assertEqual(self.content.subject, self.subject)

    def test_content_deletion_cascade(self):
        """Test if deleting Subject deletes related Contents (CASCADE)."""
        content_id = self.content.content_id
        self.subject.delete()
        with self.assertRaises(Content.DoesNotExist):
            Content.objects.get(content_id=content_id)

    def test_subject_update_reflects_in_content(self):
        """Test if updating the Subject reflects in the Content relationship."""
        self.subject.subject_name = "Natural Sciences"
        self.subject.save()
        self.content.refresh_from_db()
        self.assertEqual(self.content.subject.subject_name, "Natural Sciences")
    
    def test_field_max_lengths(self):
        """Test max length constraints of fields."""
        title = Content._meta.get_field('content_title')
        self.assertEqual(title.max_length, 50)
        desc = Content._meta.get_field('content_desc')
        self.assertEqual(desc.max_length, 100)


class ActivityModelTest(TestCase):

    def setUp(self):
        """Set up test data before each test."""
        # Create a subject first
        self.subject = Subject.objects.create(
            subject_name="Biology",
            subject_image="biology.jpg",
            subject_desc="Study of living organisms"
        )
        
        # Create a content associated with the subject
        self.content = Content.objects.create(
            subject=self.subject,
            content_title="Ecosystems",
            content_desc="Explore different ecosystems",
            content_icon="ecosystem.svg"
        )
        
        # Create an activity associated with the content
        self.activity = Activity.objects.create(
            content=self.content,
            activity_title="Build a Farm",
            activity_icon="farm.svg",
            scene_file_name="farm.tscn"
        )

    def test_activity_creation(self):
        """Test if an Activity instance is created correctly."""
        self.assertEqual(self.activity.activity_title, "Build a Farm")
        self.assertEqual(str(self.activity.activity_icon), "farm.svg")
        self.assertEqual(self.activity.scene_file_name, "farm.tscn")

    def test_activity_str_method(self):
        """Test the __str__ method of Activity model."""
        self.assertEqual(str(self.activity), "Build a Farm")

    def test_activity_auto_id(self):
        """Test if activity_id is auto-generated."""
        self.assertIsNotNone(self.activity.activity_id)

    def test_created_at_field(self):
        """Test if created_at is automatically set."""
        self.assertIsNotNone(self.activity.created_at)

    def test_foreign_key_relation(self):
        """Test if the ForeignKey is correctly assigned."""
        self.assertEqual(self.activity.content, self.content)

    def test_activity_deletion_cascade(self):
        """Test if deleting Content deletes related Activities (CASCADE)."""
        activity_id = self.activity.activity_id
        self.content.delete()
        with self.assertRaises(Activity.DoesNotExist):
            Activity.objects.get(activity_id=activity_id)

    def test_content_update_reflects_in_activity(self):
        """Test if updating the Content reflects in the Activity relationship."""
        self.content.content_title = "Biomes"
        self.content.save()
        self.activity.refresh_from_db()
        self.assertEqual(self.activity.content.content_title, "Biomes")
    
    def test_field_max_lengths(self):
        """Test max length constraints of fields."""
        title = Activity._meta.get_field('activity_title')
        self.assertEqual(title.max_length, 100)
        scene_file = Activity._meta.get_field('scene_file_name')
        self.assertEqual(scene_file.max_length, 100)
    
    def test_optional_scene_file(self):
        """Test that scene_file_name is optional."""
        activity = Activity.objects.create(
            content=self.content,
            activity_title="Interactive Quiz",
            activity_icon="quiz.svg",
            scene_file_name=None
        )
        self.assertIsNone(activity.scene_file_name)