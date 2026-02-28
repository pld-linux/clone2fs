Summary:	Copy an entire ext2/ext3 file system
Summary(pl.UTF-8):	Kopiowanie całego systemu plików ext2/ext3
Name:		clone2fs
Version:	1.3.0
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.mr511.de/software/%{name}-%{version}.tar.gz
# Source0-md5:	0454af6d16a2baf506850c7bb13bebcb
URL:		http://www.mr511.de/software/english.html
BuildRequires:	e2fsprogs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clone2fs is a program that copies an ext2/ext3 file system to another
volume or an image file.

%description -l pl.UTF-8
clone2fs to program kopiujący system plików ext2/ext3 na inny dysk lub
do pliku obrazu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -fno-strict-aliasing -Wall" \
	LIBE2FS_LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	sbindir=$RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) /sbin/clone2fs
