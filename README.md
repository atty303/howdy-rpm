# howdy-rpm

これはFedora 43向けにビルドしたHowdyのRPMパッケージです。
https://github.com/principis/copr-specs をベースにしています。

## 利用方法

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

## 開発

### Prerequisite

- podman
- mise

### ビルド方法

1. このリポジトリをクローンします。
2. `mise run build`でビルドします。

### リリース

semantic-releaseを使用しています。
