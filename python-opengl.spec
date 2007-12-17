%define	libname		PyOpenGL
%define	name		python-opengl
%define	version		2.0.1.09
%define	release		%mkrel 7

Summary:	Python bindings for OpenGL
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD
Group:		System/Libraries
URL:		http://pyopengl.sourceforge.net/
Source:		%{libname}-%{version}.tar.bz2
BuildRequires:	python-devel, mesaglut-devel
BuildRequires:	tcl tcl-devel tk tk-devel
BuildRequires:  xorg-x11-Xvfb xorg-x11-xauth 

%description
Python bindings for OpenGL

%package doc
Summary: Documentation files for %{name}
Group: Development/Python

%description doc
Documentation files for %{name}

%prep
%setup -n %{libname}-%{version} -q
perl -pi -e 's|/lib|/%_lib|g' ./config/linux.cfg  

%build
XDISPLAY=$(i=2; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%{_prefix}/bin/Xvfb :$XDISPLAY &
export DISPLAY=:$XDISPLAY
xauth add $DISPLAY . EE

python setup.py build

kill $(cat /tmp/.X$XDISPLAY-lock)

%install
rm -rf %{buildroot}
mv OpenGL/doc/ .
XDISPLAY=$(i=2; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
%{_prefix}/bin/Xvfb :$XDISPLAY &
export DISPLAY=:$XDISPLAY
xauth add $DISPLAY . EE

python setup.py install --prefix=%{buildroot}/%{_prefix}

kill $(cat /tmp/.X$XDISPLAY-lock)

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/python%{pyver}/site-packages/*OpenGL*


%files doc
%defattr(-,root,root)
%doc doc/*


