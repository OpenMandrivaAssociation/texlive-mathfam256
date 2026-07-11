%global tl_name mathfam256
%global tl_revision 53519

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Extend math family up to 256 for pLaTeX/upLaTeX/Lamed
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mathfam256
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfam256.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mathfam256.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package increases the upper limit of math symbols up to 256, using
\omath... primitives. These primitives were originally introduced in
Omega and are currently available in the following formats: pLaTeX (runs
on e-pTeX), upLaTeX (runs on e-upTeX), Lamed (runs on Aleph, successor
of Omega).

