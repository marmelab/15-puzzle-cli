<table>
        <tr>
            <td><img width="120" src="https://cdnjs.cloudflare.com/ajax/libs/octicons/8.5.0/svg/rocket.svg" alt="onboarding" /></td>
            <td><strong>Archived Repository</strong><br />
            The code of this repository was written during a <a href="https://marmelab.com/blog/2018/09/05/agile-integration.html">Marmelab agile integration</a>. It illustrates the efforts of a new hiree, who had to implement a board game in several languages and platforms as part of his initial learning. Some of these efforts end up in failure, but failure is part of our learning process, so the code remains publicly visible.<br />
        <strong>This code is not intended to be used in production, and is not maintained.</strong>
        </td>
        </tr>
</table>

# 15-puzzle-cli

A cli tool to play the 15-puzzle game, in Python.

> See the [related article](https://marmelab.com/blog/2017/10/25/jeu-du-taquin-en-python.html) on the Marmelab blog

## Help

Print all available commands

```bash
make
```

## Build

Build the docker

```bash
make install
```

## Run the game

Run the 15-puzzle game

```bash
make run
```

## Contributing

### Test

Run all tests

```bash
make test
```

### Linter

Run the pep8 linter

```bash
make lint
```
