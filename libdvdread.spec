Summary:	Library to read DVD images
Summary(pl):	Biblioteka do odczytu obrazów DVD-Video
Name:		libdvdread
Version:	0.9.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.dtek.chalmers.se/groups/dvd/%{name}-%{version}.tar.gz
Patch0:		%{name}-alpha.patch
URL:		http://www.dtek.chalmers.se/groups/dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdread provides a simple foundation for reading DVD-Video images.

For reading CSS-encrypted DVDs you will also need libdvdcss package.

%description -l pl
Biblioteka dostarczaj±ca prosty interfejs do odczytu obrazów
DVD-Video.

Aby czytaæ p³yty DVD szyfrowane CSS potrzebny jest tak¿e pakiet
libdvdcss.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag³ówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
dvd w swoich programach.

%package static
Summary:	libdevdread static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu DVD-Video
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is package with static libdvdread libraries.

%description static -l pl
Statyczne biblioteki libdvdread.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
automake -a
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS TODO NEWS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/dvdread

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
