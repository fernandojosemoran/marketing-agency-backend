CKEDITOR_APPS = [
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
             'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'autoParagraph': False,
    },
}


CKEDITOR_UPLOAD_PATH = "/media/"
