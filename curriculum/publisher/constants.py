"""Constants for curriculum publishing."""

# Dependency order for curriculum synchronization
SYNCED_MODEL_NAMES = [
    # Top-level natural-key models
    'Curriculum',
    'Grade',
    'Subject',
    # Subject-level configuration
    'PedagogyTemplate',
    'GenerationRule',
    'KnowledgePack',
    'KnowledgeChunk',
    # Curriculum hierarchy
    'Topic',
    'LearningUnit',
    # Semantic knowledge layer
    'Concept',
    'ConceptRelationship',
    'LearningObjective',
    'Misconception',
    # Lesson content
    'Lesson',
    'LessonBlock',
    'LessonAsset',
    # Experience graphs & simulations
    'LearningExperienceGraph',
    'Simulation',
]

# Operational models that must NEVER be touched during curriculum publishing
PROTECTED_OPERATIONAL_MODELS = [
    # Resources
    'User',
    'UserProfile',
    'StudentSubjectSelection',
    'StudentAcademicBaseline',
    'Category',
    'ExperimentVideo',
    'VideoInteraction',
    'AccessToken',
    'UploadedFile',
    'Invitation',
    'PasswordResetToken',
    # Questions
    'Quiz',
    'Question',
    'Answer',
    'QuestionAttempt',
    'StudentAnswer',
    # Organizations
    'School',
    'OrganizationMembership',
    'AcademicYear',
    'SchoolClass',
    'Stream',
    'TeacherSubjectAssignment',
    'TeacherStreamAssignment',
    'StudentEnrollment',
    'SchoolSubscription',
    'SchoolInvitation',
    'UnverifiedSchoolSuggestion',
    'AcademicExamination',
    'AcademicResultSheet',
    'BackgroundProcessingTask',
    # Subscriptions & Billing
    'Product',
    'ProductVariant',
    'AccessScope',
    'SubscriptionPlan',
    'Subscription',
    'SubscriptionSubject',
    'Promotion',
    'PromotionRedemption',
    'Invoice',
    'InvoiceItem',
    'InvoicePaymentTransaction',
    'MpesaPaymentAccount',
    'MpesaApiAccessToken',
    'FinancialLedgerEntry',
    # Curriculum operational/runtime models
    'GenerationJob',
    'LearningSession',
    'RuntimeNodeProgress',
]
