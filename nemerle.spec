Summary:	Nemerle compiler
Summary(pl):	Kompilator jêzyka Nemerle
Name:		nemerle
Version:	0.1.4
Release:	2
Epoch:		0
License:	BSD
Group:		Development/Languages
Vendor:		Nemerle Development Team <feedback@nemerle.org>
Source0:	http://nemerle.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	021fd226df9816f79a912df6bbe70cc3
# uses %{_libdir}, so seems not to be noarch
#BuildArch:	noarch
URL:		http://nemerle.org/
Requires(post):	mono >= 0.31
Requires:	mono >= 0.31
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nemerle is a new functional language designed from the ground up for
the .NET platform. Nemerle supports: object oriented and imperative
.NET concepts, variant datatypes, matching, higher order functions and
powerful macro system. It has simple, C#-like syntax and makes access
to imperative features easy, and thus is easy to learn.

%description -l pl
Nemerle jest nowym jêzykiem funkcjonalnym zaprojektowym od pocz±tku z
my¶l± o platformie .NET. Nemerle wspiera programowanie obiektowe i
imperatywne, typy wariantowe, dopasowanie wzorca, funkcje wy¿szych
rzêdów oraz pote¿ny system makr. Sk³adnia Nemerle jest prosta,
przypomina trochê C#. Nemerle umo¿liwa ³atwy dostêp do swych
imperatywnych oraz obiektowych cech, co powinno u³atwiæ uczenie siê
go.

%package libs
Summary:	Nemerle runtime environment
Summary(pl):	¦rodowisko uruchomieniowe jêzyka Nemerle
BuildArch:	noarch
Group:		Libraries
Requires(post):	mono >= 0.29
Requires:	mono >= 0.29

%description libs
Libraries needed to run programs written in Nemerle.

%description libs -l pl
Biblioteki niezbêdne do uruchamiania programów napisanych w Nemerle.

%prep
%setup -q

%build
./configure \
	--ignore-errors \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.exe $RPM_BUILD_ROOT%{_libdir}/*.dll ; do
	touch $f.so
done

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r snippets/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
mono --aot %{_libdir}/Nemerle.Compiler.dll || :
mono --aot %{_libdir}/Nemerle.Macros.dll || :
mono --aot %{_bindir}/ncc.exe || :

%post libs
mono --aot %{_libdir}/Nemerle.dll || :

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README doc/html misc/*.{vim,el}
%attr(755,root,root) %{_bindir}/ncc
%attr(755,root,root) %{_bindir}/ncc.exe
%attr(755,root,root) %{_libdir}/Nemerle.Macros.dll
%attr(755,root,root) %{_libdir}/Nemerle.Compiler.dll
%ghost %attr(755,root,root) %{_bindir}/ncc.exe.so
%ghost %attr(755,root,root) %{_libdir}/Nemerle.Macros.dll.so
%ghost %attr(755,root,root) %{_libdir}/Nemerle.Compiler.dll.so
%{_mandir}/man1/*
%{_examplesdir}/%{name}-%{version}

%files libs
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) %{_libdir}/Nemerle.dll
%ghost %attr(755,root,root) %{_libdir}/Nemerle.dll.so
