%define	libname PyOpenGL

Summary:	Python bindings for OpenGL
Name:		python-opengl
Version:	3.0.1
Release:	%mkrel 2
License:	BSD
Group:		System/Libraries
URL:		http://pyopengl.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyopengl/%{libname}-%{version}.tar.gz
Patch0:		PyOpenGL-3.0.0a6-shebang.patch
BuildRequires:	mesaglut-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRequires:	tk
BuildRequires:	tk-devel
BuildRequires:	python-setuptools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%patch0 -p0 -z .shebang

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*OpenGL*
%exclude %{python_sitelib}/OpenGL/Tk

%files tk
%defattr(-,root,root,-)
%{python_sitelib}/OpenGL/Tk

%files doc
%defattr(-,root,root,-)
