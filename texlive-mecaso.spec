%global tl_name mecaso
%global tl_revision 60346

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Formulas frequently used in rigid body mechanics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mecaso
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mecaso.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mecaso.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a number of formulas frequently used in rigid body
mechanics. Since most of these formulas are long and tedious to write,
this package wraps them up in short commands.

