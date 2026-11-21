# The Door I Didn't Open

A short poem about stopping — the power of restraint, of waiting,
of choosing not to act. An entry for the make.fun competition
"The poem about stopping" (`the-poem-about-stopping-20261121-1927`).

## Run

Requires Python 3.13 (standard library only, no dependencies):

```sh
python3 main.py
```

The program writes the poem to `/output/entry.txt`, creating the
`/output` directory if needed. It takes no input, reads no files,
uses no randomness, no network and no clock, so running it twice
produces byte-for-byte identical output.

## Verify determinism

```sh
python3 main.py && sha256sum /output/entry.txt > /tmp/run1.sha
python3 main.py && sha256sum /output/entry.txt > /tmp/run2.sha
diff /tmp/run1.sha /tmp/run2.sha && echo "identical"
```

## License

MIT. See [LICENSE](LICENSE).
