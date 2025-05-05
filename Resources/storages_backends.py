from storages.backends.s3boto3 import S3Boto3Storage
from cloudinary_storage.storage import MediaCloudinaryStorage

class CloudflareR2Storage(S3Boto3Storage):
    bucket_name = 'vizlearn'
    default_acl = 'public-read'

class CloudinaryStorage(MediaCloudinaryStorage):
    pass
