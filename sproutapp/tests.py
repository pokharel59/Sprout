# from django.test import TestCase
# from sproutapp.models import Subject, Content, Activity # Import the Subject model

# class SubjectModelTest(TestCase):

#     def setUp(self):
#         """Set up test data before each test."""
#         self.subject = Subject.objects.create(
#             subject_name="Mathematics",
#             subject_image="math.png",
#             subject_desc="This is a math subject"
#         )

#     def test_subject_creation(self):
#         """Test if a Subject instance is created correctly."""
#         self.assertEqual(self.subject.subject_name, "Mathematics")
#         self.assertEqual(self.subject.subject_image, "math.png")
#         self.assertEqual(self.subject.subject_desc, "This is a math subject")

#     def test_subject_str_method(self):
#         """Test the __str__ method of Subject model."""
#         self.assertEqual(str(self.subject), "Mathematics")

#     def test_subject_auto_id(self):
#         """Test if subject_id is auto-generated."""
#         self.assertIsNotNone(self.subject.subject_id)

#     def test_created_at_field(self):
#         """Test if created_at is automatically set."""
#         self.assertIsNotNone(self.subject.created_at)


# class ContentModelTest(TestCase):

#     def setUp(self):
#         """Create a subject instance"""
#         self.subject = Subject.objects.create(subject_name="Science")

#         """Set up test data before each test."""
#         self.content = Content.objects.create(
#             subject = self.subject,
#             content_title="Physics",
#             content_desc="This is physics of science",
#             content_icon="physics.svg"
#         )

#     def test_content_creation(self):
#         """Test if a Content instance is created correctly."""
#         self.assertEqual(self.content.content_title, "Physics")
#         self.assertEqual(self.content.content_desc, "This is physics of science")
#         self.assertEqual(self.content.content_icon, "physics.svg")

#     def test_content_str_method(self):
#         """Test the __str__ method of Content model."""
#         self.assertEqual(str(self.content), "Physics")

#     def test_content_auto_id(self):
#         """Test if content_id is auto-generated."""
#         self.assertIsNotNone(self.content.content_id)

#     def test_created_at_field(self):
#         """Test if created_at is automatically set."""
#         self.assertIsNotNone(self.content.created_at)

#     def test_foreign_key_relation(self):
#         """Test if the ForeignKey is correctly assigned."""
#         self.assertEqual(self.content.subject, self.subject)

#     def test_content_deletion_cascade(self):
#         """Test if deleting Subject deletes related Contens (CASCADE)."""
#         self.subject.delete()
#         self.assertEqual(Content.objects.count(), 0) # All contents should be deleted

#     def test_subject_update_reflects_in_content(self):
#         """Test if updating the Subject reflects in the Content relationship."""
#         self.subject.subject_name = "Social"
#         self.subject.save()
#         self.content.refresh_from_db()
#         self.assertEqual(self.content.subject.subject_name, "Social")

# class ActivityModelTest(TestCase):

#     def setUp(self):
#         """Create a content instance"""
#         self.content = Content.objects.create(content_title="Biology")

#         """Set up test data before each test."""
#         self.activity = Activity.objects.create(
#             content = self.content,
#             activity_title="Build farm",
#             activity_icon="biology.svg",
#             scene_file_name="farm.tscn"
#         )

#     def test_activity_creation(self):
#         """Test if a Activity instance is created correctly."""
#         self.assertEqual(self.activity.activity_title, "Build farm")
#         self.assertEqual(self.activity.activity_icon, "biology.svg")
#         self.assertEqual(self.activity.scene_file_name, "farm.tscn")

#     def test_activity_str_method(self):
#         """Test the __str__ method of Activity model."""
#         self.assertEqual(str(self.activity), "Build farm")

#     def test_activity_auto_id(self):
#         """Test if activity_id is auto-generated."""
#         self.assertIsNotNone(self.activity.activity_id)

#     def test_created_at_field(self):
#         """Test if created_at is automatically set."""
#         self.assertIsNotNone(self.activity.created_at)

#     def test_foreign_key_relation(self):
#         """Test if the ForeignKey is correctly assigned."""
#         self.assertEqual(self.activity.content, self.content)

#     def test_activity_deletion_cascade(self):
#         """Test if deleting Activity deletes related Contens (CASCADE)."""
#         self.content.delete()
#         self.assertEqual(Activity.objects.count(), 0) # All contents should be deleted

#     def test_content_update_reflects_in_activity(self):
#         """Test if updating the Content reflects in the Activity relationship."""
#         self.content.content_title = "Build road"
#         self.content.save()
#         self.activity.refresh_from_db()
#         self.assertEqual(self.activity.content.content_title, "Build road")