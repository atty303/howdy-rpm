#!/usr/bin/env -S bash -euo pipefail

dnf install -y git rpmdevtools python3-wheel python3-cython createrepo_c

rpmdev-setuptree
rpm_root="$(rpm --eval '%_topdir')"

build_rpm() {
  local spec_path="$1"
  local spec_file
  spec_file="$(basename "$spec_path")"
  pushd "$(dirname "$spec_path")"

  find . -maxdepth 1 -type f ! -name '*.spec' -exec install -Dm0644 {} "$rpm_root/SOURCES/" \;

  dnf builddep -y "$spec_file"
  spectool -g -R "$spec_file"
  rpmbuild -ba "$spec_file"

  popd
}

for spec in */*.spec; do
  echo "Building $spec"
  build_rpm "$spec"
done

mkdir -p dist
find "$rpm_root/RPMS" -name '*.rpm' -exec cp {} dist/ \;
find "$rpm_root/SRPMS" -name '*.rpm' -exec cp {} dist/ \;
createrepo_c dist/
