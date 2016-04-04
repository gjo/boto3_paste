.. -*- coding: utf-8 -*-

===========
boto3_paste
===========

Utility for ``boto3.session.Session()``


Install
=======

from PyPI::

  pip install boto3_paste

from source::

  $ pip install .


How to use
==========

If you use ``pyramid``::

  import boto3_paste

  def main(global_config, **settings):
      boto_session = boto3_paste.session_from_config(settings)
      config = Configurator(settings=settings)

      # Some your configuration

      return config.make_wsgi_app()


Configuration Keys
==================

See ``botocore.session.Session``'s Documents.

Example ini-file::

  botocore.profile =
  botocore.region =
  botocore.data_path =
  botocore.config_file = ~/.aws/config
  botocore.ca_bunfle =
  botocore.credentials_file = ~/.aws/credentials
  botocore.metadata_service_timeout = 1
  botocore.metadata_service_num_attempts = 1
  boto3.aws_access_key_id =
  boto3.aws_secret_access_key =
  boto3.aws_session_token =
  boto3.region_name =
  boto3.profile_name =


All keys are not mandatory.
If you don't write any keys, ``botocore.session.Session`` instances are
created by ``default``.
