#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to read DVD images
Summary(pl.UTF-8):	Biblioteka do odczytu obrazów DVD-Video
Name:		libdvdread
Version:	4.1.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.mplayerhq.hu/MPlayer/releases/dvdnav/%{name}-%{version}.tar.bz2
# Source0-md5:	6dc068d442c85a3cdd5ad3da75f6c6e8
Patch0:		%{name}-alpha.patch
URL:		http://www.mplayerhq.hu/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libtool >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdread provides a simple foundation for reading DVD-Video images.

For reading CSS-encrypted DVDs you will also need libdvdcss package.

%description -l pl.UTF-8
Biblioteka dostarczająca prosty interfejs do odczytu obrazów
DVD-Video.

Aby czytać płyty DVD szyfrowane CSS potrzebny jest także pakiet
libdvdcss.

%package devel
Summary:	%{name} library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja pozwalająca na dodawanie obsługi
dvd w swoich programach.

%package static
Summary:	libdvdread static libraries
Summary(pl.UTF-8):	Statyczne biblioteki do obsługi formatu DVD-Video
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libdvdread libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libdvdread.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DEVELOPMENT-POLICY.txt README TODO
%attr(755,root,root) %{_libdir}/libdvdread.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvdread.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dvdread-config
%attr(755,root,root) %{_libdir}/libdvdread.so
%{_libdir}/libdvdread.la
%{_includedir}/dvdread
%{_pkgconfigdir}/dvdread.pc
%{_aclocaldir}/dvdread.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdread.a
%endif
