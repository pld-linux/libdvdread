#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library to read DVD images
Summary(pl.UTF-8):	Biblioteka do odczytu obrazów DVD-Video
Name:		libdvdread
Version:	7.1.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.videolan.org/pub/videolan/libdvdread/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	95048908fb1596cdc2c6cb310017aef4
URL:		http://dvdnav.mplayerhq.hu/
BuildRequires:	gcc >= 6:4.6
BuildRequires:	meson >= 0.60.0
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Suggests:	libdvdcss >= 1.2
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
Summary:	Header files for libdvread library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdvdread
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The include files and other resources you can use to incorporate
libdvdread into applications.

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

%build
%meson \
	%{!?with_static_libs:--default-library=shared}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libdvdread.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvdread.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvdread.so
%{_includedir}/dvdread
%{_pkgconfigdir}/dvdread.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdread.a
%endif
