%define	oname PyOpenGL

Summary:	Python bindings for OpenGL
Name:		python-opengl
Version:	3.1.0
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://pyopengl.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/P/PyOpenGL/PyOpenGL-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools
BuildRequires:	swig
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(tcl)
BuildRequires:	pkgconfig(tk)

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
%setup -qn %{oname}-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%files
%{py_puresitedir}/*OpenGL*
%exclude %{py_puresitedir}/OpenGL/Tk

%files tk
%{py_puresitedir}/OpenGL/Tk

%files doc

