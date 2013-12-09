django-moth-utils
=================

Utilities to automate the process of installing and monitoring django-moth

Usage
=====

The executable scripts in this repository are usually used from within a `circle.yml` file
like the one we have in the [w3af](https://raw.github.com/andresriancho/w3af/) project,
which looks like this:

```yaml
machine:
  python:
    version: 2.7.3

  post:
    # This was required to avoid issues with different builds of python being
    # used between the gtk libs installed in /usr/lib/python2.7/dist-packages/
    # and the python which was put inside my virtualenv
    - pyenv global system

    # And we want to start the django-moth server
    # https://circleci.com/docs/background-process
    - nohup bash -c "python django-moth-utils/scripts/setup_moth.py &" > $CIRCLE_ARTIFACTS/setup-moth-nohup.log

dependencies:
  cache_directories:
    # Cache the directory to avoid delays in downloading the source each time
    - "django-moth"
  pre:
    # Wait for the daemon to be available to run the tests
    - python scripts/wait_for_moth.py

test:
  override:
    - "pylint --msg-template='{msg_id}:{line:3d},{column}: {obj}: {msg}' -E scripts tests utils"

    # Run some test which uses django-moth here:
    - nosetests tests/

    # Cleanup
    - python scripts/teardown_moth.py
```

An real-life example of this can be found at our repository `circle.yml` which is used to test
that the scripts work (aah!... the recursive mayhem!).