%global tl_name exteps
%global tl_revision 19859

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.41
Release:	%{tl_revision}.1
Summary:	Include EPS figures in MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/exteps
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/exteps.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Exteps is a module for including external EPS figures into MetaPost
figures. It is written entirely in MetaPost, and does not therefore
require any post processing of the MetaPost output.

