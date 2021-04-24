#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library to read DVD images
Summary(pl.UTF-8):	Biblioteka do odczytu obrazów DVD-Video
Name:		libdvdread
Version:	6.1.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://download.videolan.org/pub/videolan/libdvdread/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	034581479968405ed415c34a50d00224
URL:		http://dvdnav.mplayerhq.hu/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6
BuildRequires:	libtool >= 2:2
BuildRequires:	tar >= 1:1.22
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
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libdvdread.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvdread.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvdread.so
%{_libdir}/libdvdread.la
%{_includedir}/dvdread
%{_pkgconfigdir}/dvdread.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdread.a
%endif
