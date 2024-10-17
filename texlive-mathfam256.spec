Name:		texlive-mathfam256
Version:	53519
Release:	2
Summary:	Extend math family up to 256 for pLaTeX/upLaTeX/Lamed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathfam256
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfam256.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfam256.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package increases the upper limit of math symbols up to
256, using \omath... primitives. These primitives were
originally introduced in Omega and are currently available in
the following formats: pLaTeX (runs on e-pTeX), upLaTeX (runs
on e-upTeX), Lamed (runs on Aleph, successor of Omega).

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mathfam256
%doc %{_texmfdistdir}/doc/latex/mathfam256

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
