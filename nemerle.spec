# TODO: antlr should install antlr.runtime.dll, and this
# package should use it
Summary:	Nemerle compiler
Summary(pl):	Kompilator jêzyka Nemerle
Name:		nemerle
Version:	0.3.2
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages
Vendor:		Nemerle Development Team <feedback@nemerle.org>
Source0:	http://nemerle.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	33263c735a6975fe8eb640fa6074aff9
URL:		http://nemerle.org/
BuildRequires:	antlr
BuildRequires:	mono-devel >= 1.1.6-2
BuildRequires:  nant
BuildRequires:	pkgconfig
Requires:	mono-devel >= 1.1.6-2
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
Requires:	mono >= 1.1.6-2

%description libs
Libraries needed to run programs written in Nemerle.

%description libs -l pl
Biblioteki niezbêdne do uruchamiania programów napisanych w Nemerle.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_prefix}/lib \
	--mandir=%{_mandir}/man1 \
	--disable-aot \
	--pkgconfigdir=%{_pkgconfigdir} \
	--net-engine=mono
%{__make}
%{__make} check
%{__make} -C snippets clean

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
%attr(755,root,root) %{_bindir}/cs2n
%attr(755,root,root) %{_bindir}/cs2n.exe
%attr(755,root,root) %{_bindir}/nemish
%attr(755,root,root) %{_bindir}/nemish.exe
%{_prefix}/lib/mono/nemerle
%{_prefix}/lib/mono/gac/Nemerle.*
%{_prefix}/lib/mono/gac/antlr*
%{_datadir}/NAnt/bin/Nemerle.NAnt.Tasks.*
%{_mandir}/man1/*
%{_pkgconfigdir}/nemerle.pc
%{_examplesdir}/%{name}-%{version}

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%{_prefix}/lib/mono/gac/Nemerle
