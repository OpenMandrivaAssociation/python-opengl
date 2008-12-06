%define beta b5
%define	libname PyOpenGL

Summary:	Python bindings for OpenGL
Name:		python-opengl
Version:	3.0.0
Release:	%mkrel 0.0.%{beta}.2
License:	BSD
Group:		System/Libraries
URL:		http://pyopengl.sourceforge.net/
Source0:	http://downloads.sourceforge.net/pyopengl/%{libname}-%{version}%{beta}.tar.gz
Patch0:		PyOpenGL-3.0.0a6-shebang.patch
BuildRequires:	mesaglut-devel
BuildRequires:	python-devel
BuildRequires:	swig
BuildRequires:	tcl
BuildRequires:	tcl-devel
BuildRequires:	tk
BuildRequires:	tk-devel
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

%setup -q -n %{libname}-%{version}%{beta}
%patch0 -p1 -z .shebang

perl -pi -e 's|/lib|/%_lib|g' ./config/linux.cfg  

%build
python setup.py build

%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot} --prefix=%{_prefix} --single-version-externally-managed

# don't package the tests files
rm -r %{buildroot}%{python_sitelib}/OpenGL/tests

# for %%doc
rm documentation/pydoc/builddocs.py documentation/buildepydoc.py

# fix deps
chmod 644 %{buildroot}%{python_sitelib}/%{libname}-%{version}%{beta}-py*.egg-info/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc license.txt
%{python_sitelib}/*OpenGL*
%exclude %{python_sitelib}/OpenGL/Tk

%files tk
%defattr(-,root,root,-)
%{python_sitelib}/OpenGL/Tk

%files doc
%defattr(-,root,root,-)
%doc documentation/*
