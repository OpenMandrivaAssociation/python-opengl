%define	libname PyOpenGL

Summary:	Python bindings for OpenGL
Name:		python-opengl
Version:	3.0.2
Release:	1
License:	BSD
Group:		System/Libraries
URL:		http://pyopengl.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-%{version}.tar.gz
BuildRequires:	mesa-common-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	python-setuptools
BuildArch:      noarch

%description
Python bindings for OpenGL

%package	tk
Summary:	PyOpenGL Tk widget
Group:		System/Libraries
Requires:	%{name} = %{version}
Requires:	tkinter

%description	tk
PyOpenGL Togl (Tk OpenGL widget) 1.6 support.

%package	doc
Summary:	Documentation files for %{name}
Group:		Development/Python

%description	doc
Documentation files for %{name}

%prep

%setup -q -n %{libname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%{py_puresitedir}/*OpenGL*
%exclude %{py_puresitedir}/OpenGL/Tk

%files tk
%defattr(-,root,root,-)
%{py_puresitedir}/OpenGL/Tk

%files doc
%defattr(-,root,root,-)


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0.1-2mdv2011.0
+ Revision: 668020
- mass rebuild

* Sun Oct 31 2010 John Balcaen <mikala@mandriva.org> 3.0.1-1mdv2011.0
+ Revision: 590956
- Update to 3.0.1 final
- rediff patch0
- rebuild for python2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3.0.1-0.0.a3.2mdv2010.1
+ Revision: 523851
- rebuilt for 2010.1

* Tue Aug 25 2009 Lev Givon <lev@mandriva.org> 3.0.1-0.0.a3.1mdv2010.0
+ Revision: 421272
- Update to 3.0.1a3.

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 3.0.0-0.0.b8.1mdv2009.1
+ Revision: 318920
- new verrsion 3.0.0 b8

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 3.0.0-0.0.b5.3mdv2009.1
+ Revision: 318899
- rebuild for new python

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 3.0.0-0.0.b5.2mdv2009.1
+ Revision: 311088
- buildrequires python-setuptools
- drop a now useless lib64 workaround
- rebuild for new tcl
- requires fonts-ttf-dejavu
- use modified tarball with non-free font Test.ttf (actually Arial) replaced by a symlink to a DejaVu font (#38259)
- clean up spec a bit

  + Oden Eriksson <oeriksson@mandriva.com>
    - 3.0.0b5
    - sync with fedora
    - drop the Xvfb stuff, it's borked

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.0.1.09-7mdv2008.1
+ Revision: 136454
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - BR swig
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 07 2006 Götz Waschk <waschk@mandriva.org> 2.0.1.09-7mdv2007.0
+ Revision: 91905
- fix buildrequires
- bot rebuild
- Import python-opengl

* Wed Dec 06 2006 Götz Waschk <waschk@mandriva.org> 2.0.1.09-6mdv2007.1
- update file list

* Mon Jul 03 2006 Emmanuel Andry <eandry@mandriva.org> 2.0.1.09-5mdv2007.0
- %%mkrel
- fix deps

* Wed Jan 04 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.1.09-4mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Sun May 15 2005 Michael Scherer <misc@mandriva.org> 2.0.1.09-3mdk
- fix buildrequires to please mr lurt
- fix build on amd64 to please miss deborah

* Sat May 14 2005 Michael Scherer <misc@mandriva.org> 2.0.1.09-2mdk
- from Tigrux <tigrux@ximian.com>
  - Do not require python = 2.5

* Tue Dec 07 2004 Michael Scherer <misc@mandrake.org> 2.0.1.09-1mdk
- allows build without X
- from Tigrux <tigrux@ximian.com> 2.0.1.09-1
  - First rpm for Mandrake


