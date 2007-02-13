#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to read DVD images
Summary(pl.UTF-8):	Biblioteka do odczytu obrazów DVD-Video
Name:		libdvdread
Version:	0.9.7
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	078788c9241ae16763529e1235502337
Patch0:		%{name}-alpha.patch
Patch1:		%{name}-UDFFindFile.patch
URL:		http://www.dtek.chalmers.se/groups/dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

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
%doc README AUTHORS TODO NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/dvdread

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
