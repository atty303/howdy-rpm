# howdy-rpm

This is a [Howdy](https://github.com/boltgolt/howdy) RPM package built for Fedora 43, based on https://github.com/principis/copr-specs.

I only tested it with Bazzite.

## Background

Howdy requires `python-dlib`, which is no longer available in Fedora 43. Therefore, it is built from source.

## Installation

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

### [BlueBuild](https://blue-build.org/)

You can use the following recipe.yml.

```yaml
# recipe.yml
modules:
  - type: dnf
    repos:
      cleanup: true
      files:
        add:
          - https://raw.githubusercontent.com/atty303/howdy-rpm/refs/heads/main/howdy.repo
    install:
      packages:
        - howdy
```

## Usage

See https://github.com/boltgolt/howdy.

## Development

### Prerequisite

- podman
- mise

### How to build

1. Clone this repository.
2. Build with `mise run build`.

Build artifacts are in `dist/`.

### Release

Using semantic-release.

## Maintenance policy

I created this for my own use, so I will continue to maintain it as long as I use it.

## References

- https://copr.fedorainfracloud.org/coprs/principis/howdy-beta/
- https://github.com/principis/copr-specs/pull/11
- https://github.com/rall/blue-howdy