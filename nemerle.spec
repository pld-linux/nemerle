%define _rev 1418
Summary:	Nemerle compiler
Summary(pl):	Kompilator jêzyka Nemerle
Name:		nemerle
Version:	0.0.1.%{_rev}
Release:	1
Epoch:		0
License:	BSD
Group:		Development/Languages
Vendor:		Nemerle Development Team <feedback@nemerle.org>
Source0:	http://nemerle.org/download/%{name}-%{_rev}.tar.gz
# Source0-md5:	f728c023ba373f2c55586e84c4086b39
BuildArch:	noarch
URL:		http://nemerle.org/
Requires(post):	mono >= 0.29
Requires:	mono >= 0.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nemerle is a new functional language designed from the ground up for
the .NET platform. Nemerle supports: object oriented and imperative
.NET concepts, variant datatypes, matching, higher order functions and
powerful macro system. It has simple, C-like syntax and makes access
to imperative features easy, and thus is easy to learn.

%description -l pl
Nemerle jest nowym jêzykiem funkcjonalnym zaprojektowym od pocz±tku z
my¶l± o platformie .NET. Nemerle wspiera programowanie obiektowe i
imperatywne, typy wariantowe, dopasowanie wzorca, funkcje wy¿szych
rzêdów oraz pote¿ny system makr. Sk³adnia Nemerle jest prosta,
przypomina trochê C. Nemerle umo¿liwa ³atwy dostêp do swych
imperatywnych oraz obiektowych cech, co powinno u³atwiæ uczenie siê
go.

%package libs
Summary:	Nemerle runtime environment
Summary(pl):	¦rodowisko uruchomieniowe jêzyka Nemerle
BuildArch:	noarch
Group:		Libraries

%description libs
Libraries needed to run programs written in Nemerle.

%description libs -l pl
Biblioteki niezbêdne do uruchamiania programów napisanych w Nemerle.

%prep
%setup -q -n %{name}-%{_rev}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir}}

install boot/*.dll $RPM_BUILD_ROOT%{_libdir}
install lib/aliases.n $RPM_BUILD_ROOT%{_libdir}
install boot/ncc.exe $RPM_BUILD_ROOT%{_bindir}

for f in $RPM_BUILD_ROOT%{_bindir}/*.exe $RPM_BUILD_ROOT%{_libdir}/*.dll ; do
	touch $f.so
done

cat > $RPM_BUILD_ROOT%{_bindir}/ncc <<EOF
#!/bin/sh
mono %{_bindir}/ncc.exe "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
mono --aot %{_libdir}/Nemerle.Compiler.dll || :
mono --aot %{_libdir}/stdmacros.dll || :
mono --aot %{_bindir}/ncc.exe || :

%post libs
mono --aot %{_libdir}/Nemerle.dll || :

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/ncc
%attr(755,root,root) %{_bindir}/ncc.exe
%attr(755,root,root) %{_libdir}/stdmacros.dll
%attr(755,root,root) %{_libdir}/Nemerle.Compiler.dll
%{_libdir}/aliases.n
%ghost %attr(755,root,root) %{_bindir}/ncc.exe.so
%ghost %attr(755,root,root) %{_libdir}/stdmacros.dll.so
%ghost %attr(755,root,root) %{_libdir}/Nemerle.Compiler.dll.so

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_libdir}/Nemerle.dll
%ghost %attr(755,root,root) %{_libdir}/Nemerle.dll.so
