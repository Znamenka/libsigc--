# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	The Typesafe Signal Framework for C++
Summary(pl):	�rodowisko sygna��w z kontrol� typ�w dla C++
Name:		libsigc++
Version:	2.0.15
Release:	1
Epoch:		1
License:	LGPL
Vendor:		Karl E. Nelson <kenelson@ece.ucdavis.edu>
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsigc++/2.0/%{name}-%{version}.tar.bz2
# Source0-md5:	3da57e8fd00644390447b372e5d6103a
URL:		http://libsigc.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	perl-base
Obsoletes:	libsigc++-examples
Conflicts:	libsigc++ < 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. Originally
part of the Gtk-- widget set, libsigc++ is now a seperate library to
provide for more general use. It is the most complete library of its
kind with the ablity to connect an abstract callback to a class
method, function, or function object. It contains adaptor classes for
connection of dissimilar callbacks and has an ease of use unmatched by
other C++ callback libraries.

%description -l pl
Ta biblioteka jest implementacj� pe�nego systemu callback�w do
u�ywania w bibliotekach widget�w, interfejsach abstrakcyjnych i
og�lnym programowaniu. Oryginalnie by�a to cz�� zestawu widget�w
Gtk--, ale jest teraz oddzieln� bibliotek� og�lniejszego
przeznaczenia. Jest to kompletna biblioteka tego typu z mo�liwo�ci�
��czenia abstrakcyjnych callback�w z metodami klas, funkcjami lub
obiektami funkcji. Zawiera klasy adapter�w do ��czenia r�nych
callback�w.

%package devel
Summary:	Development tools for the Typesafe Signal Framework for C++
Summary(pl):	Narz�dzia programistyczne do �rodowiska libsig++
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel
Requires:	m4

%description devel
Development tools for the Typesafe Signal Framework for C++.

%description devel -l pl
Narz�dzia programistyczne do �rodowiska libsigc++ - sygna��w z
kontrol� typ�w.

%package doc
Summary:	Reference documentation for libsigc++
Summary(pl):	Szczeg�owa dokumentacja dla libsigc++
Group:		Documentation

%description doc
Reference documentation for libsigc++.

%description doc -l pl
Szczeg�owa dokumentacja dla libsigc++.

%package static
Summary:	Static Typesafe Signal Framework for C++ libraries
Summary(pl):	Statyczna biblioteka libsigc++
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Typesafe Signal Framework for C++ libraries.

%description static -l pl
Statyczna biblioteka libsigc++ - �rodowiska sygna��w z kontrol� typ�w.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I scripts
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/libsigc-2.0/docs devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/sigc++-*
%{_libdir}/sigc++*
%{_pkgconfigdir}/*

%files doc
%defattr(644,root,root,755)
%doc devel-docs/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
