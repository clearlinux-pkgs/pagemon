#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : pagemon
Version  : 0.02.01
Release  : 1
URL      : https://github.com/ColinIanKing/pagemon/archive/refs/tags/V0.02.01.tar.gz
Source0  : https://github.com/ColinIanKing/pagemon/archive/refs/tags/V0.02.01.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pagemon-bin = %{version}-%{release}
Requires: pagemon-data = %{version}-%{release}
Requires: pagemon-license = %{version}-%{release}
Requires: pagemon-man = %{version}-%{release}
BuildRequires : pkgconfig(ncursesw)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
pagemon
pagemon is an interactive memory/page monitoring tool allowing one to browse
the memory map of an active running process on Linux.

%package bin
Summary: bin components for the pagemon package.
Group: Binaries
Requires: pagemon-data = %{version}-%{release}
Requires: pagemon-license = %{version}-%{release}

%description bin
bin components for the pagemon package.


%package data
Summary: data components for the pagemon package.
Group: Data

%description data
data components for the pagemon package.


%package license
Summary: license components for the pagemon package.
Group: Default

%description license
license components for the pagemon package.


%package man
Summary: man components for the pagemon package.
Group: Default

%description man
man components for the pagemon package.


%prep
%setup -q -n pagemon-0.02.01
cd %{_builddir}/pagemon-0.02.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688651161
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1688651161
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pagemon
cp %{_builddir}/pagemon-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pagemon/4cc77b90af91e615a64ae04893fdffa7939db84c || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pagemon

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/pagemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pagemon/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/pagemon.8.gz
