# API Gateway to Kinesis and/or Firehose streams

[![PyPI](https://img.shields.io/pypi/v/humilis-stream-gtw.svg?style=flat)](https://pypi.python.org/pypi/humilis-stream-gtw)


[humilis]: https://github.com/humilis/humilis


## Installation


```
pip install humilis-stream-gtw
```


To install the development version:

```
pip install git+https://github.com/humilis/humilis-stream-gtw
```


## Development

Assuming you have [virtualenv][venv] installed:

[venv]: https://virtualenv.readthedocs.org/en/latest/

```
make develop
```

Configure humilis:

```
make configure
```


## Testing

You can test the deployment with:

```
make test
```

If the tests break, you can make sure you are not leaving any infrastructure
behind with:

```bash
make delete
```


## More information

See [humilis][humilis] documentation.

[humilis]: https://github.com/humilis/blob/master/README.md


## Contact

If you have questions, bug reports, suggestions, etc. please create an issue on
the [GitHub project page][github].

[github]: http://github.com/humilis/humilis-stream-gtw


## License

This software is licensed under the [MIT license][mit].

[mit]: http://en.wikipedia.org/wiki/MIT_License

See [License file][LICENSE].

[LICENSE]: ./LICENSE.txt


© 2021 German Gomez-Herrero, [Find Hotel][fh] and others.

[fh]: http://company.findhotel.net
