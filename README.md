# howdy-rpm

This is a [Howdy](https://github.com/boltgolt/howdy) RPM package built for Fedora 43 (I am using Bazzite).
It is based on https://github.com/principis/copr-specs.

## Background

Howdy requires `python-dlib`, which is no longer available in Fedora 43. Therefore, it is built from source.

## Usage

### Blue Build

```yaml
# recipe.yml

```

### Fedora

```ini
# /etc/yum.repos.d/howdy.repo
[howdy]
name=Howdy
baseurl=https://atty303.github.io/howdy-rpm/
enabled=1
gpgcheck=0
```

```bash
sudo dnf install howdy
```

## Development

### Prerequisite

- podman
- mise

### How to build

1. Clone this repository.
2. Build with `mise run build`.

### Release

Using semantic-release.

## Maintenance

I created this for my own use, so I will continue to maintain it as long as I use it.
