Summary:	Nemerle compiler
Summary(pl):	Kompilator jêzyka Nemerle
Name:		nemerle
Version:	0.2.1
Release:	3
Epoch:		0
License:	BSD
Group:		Development/Languages
Vendor:		Nemerle Development Team <feedback@nemerle.org>
Source0:	http://nemerle.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	6108697ad6d8ba434f5a98334b8eb02e
Patch0:		%{name}-disable-aot.patch
Patch1:		%{name}-save-assembly.patch
URL:		http://nemerle.org/
BuildRequires:	mono-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	mono-devel >= 1.0
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nemerle is a new functional language designed from the ground up for
the .NET platform. Nemerle supports: object oriented and imperative
.NET concepts, variant datatypes, matching, higher order functions and
powerful macro system. It has simple, C#-like syntax and makes access
to imperative features easy, and thus is easy to learn.

%description -l pl
Nemerle jest nowym jêzykiem funkcjonalnym zaprojektowanym od pocz±tku 
z my¶l± o platformie .NET. Nemerle wspiera programowanie obiektowe 
i imperatywne, typy wariantowe, dopasowanie wzorca, funkcje wy¿szych
rzêdów oraz potê¿ny system makr. Sk³adnia Nemerle jest prosta,
przypomina trochê C#. Nemerle umo¿liwia ³atwy dostêp do swych
imperatywnych oraz obiektowych cech, co powinno u³atwiæ uczenie siê
go.

%package libs
Summary:	Nemerle runtime environment
Summary(pl):	¦rodowisko uruchomieniowe jêzyka Nemerle
Group:		Libraries
Requires:	mono >= 1.0

%description libs
Libraries needed to run programs written in Nemerle.

%description libs -l pl
Biblioteki niezbêdne do uruchamiania programów napisanych w Nemerle.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}/man1 \
%ifnarch %{ix86}
	--disable-aot \
%endif
	--net-engine=mono
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r snippets/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README doc/html misc/*.{vim,el}
%attr(755,root,root) %{_bindir}/ncc
%attr(755,root,root) %{_bindir}/ncc.exe
%{_libdir}/mono/nemerle
%{_libdir}/mono/gac/Nemerle.*
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%{_libdir}/mono/gac/Nemerle
