Summary:	Nemerle compiler
Summary(pl):	Kompilator j�zyka Nemerle
Name:		nemerle
Version:	0.2.1
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages
Vendor:		Nemerle Development Team <feedback@nemerle.org>
Source0:	http://nemerle.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	6108697ad6a8ba434f5a98f34b8eb02e
URL:		http://nemerle.org/
Requires:	mono-devel >= 1.0
BuildRequires:	mono-devel >= 1.0
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nemerle is a new functional language designed from the ground up for
the .NET platform. Nemerle supports: object oriented and imperative
.NET concepts, variant datatypes, matching, higher order functions and
powerful macro system. It has simple, C#-like syntax and makes access
to imperative features easy, and thus is easy to learn.

%description -l pl
Nemerle jest nowym j�zykiem funkcjonalnym zaprojektowanym od pocz�tku 
z my�l� o platformie .NET. Nemerle wspiera programowanie obiektowe 
i imperatywne, typy wariantowe, dopasowanie wzorca, funkcje wy�szych
rz�d�w oraz pote�ny system makr. Sk�adnia Nemerle jest prosta,
przypomina troch� C#. Nemerle umo�liwia �atwy dost�p do swych
imperatywnych oraz obiektowych cech, co powinno u�atwi� uczenie si�
go.

%package libs
Summary:	Nemerle runtime environment
Summary(pl):	�rodowisko uruchomieniowe j�zyka Nemerle
Group:		Libraries
Requires:	mono >= 1.0

%description libs
Libraries needed to run programs written in Nemerle.

%description libs -l pl
Biblioteki niezb�dne do uruchamiania program�w napisanych w Nemerle.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}/man1 \
	--net-engine=mono

%{__make}

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
