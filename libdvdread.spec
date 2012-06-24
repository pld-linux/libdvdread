Summary:	Library to read DVD images
Summary(pl):	Biblioteka do odczytu obraz�w DVD-Video
Name:		libdvdread
Version:	0.9.2
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.dtek.chalmers.se/groups/dvd/%{name}-%{version}.tar.gz
URL:		http://www.dtek.chalmers.se/groups/dvd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdread provides a simple foundation for reading DVD-Video images.

For reading CSS-encrypted DVDs you will also need libdvdcss package.

%description -l pl
Biblioteka dostarczaj�ca prosty interfejs do odczytu obraz�w
DVD-Video.

Aby czyta� p�yty DVD szyfrowane CSS potrzebny jest tak�e pakiet
libdvdcss.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag��wkowe biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%description -l pl devel
Pliki nag��wkowe oraz dokumentacja pozwalaj�ca na dodawanie obs�ugi
dvd w swoich programach.

%package static
Summary:	libdevdread static libraries
Summary(pl):	Statyczne biblioteki do obs�ugi formatu DVD-Video
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
This is package with static libdvdread libraries.

%description -l pl static
Statyczne biblioteki libdvdread.

%prep
%setup  -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
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
