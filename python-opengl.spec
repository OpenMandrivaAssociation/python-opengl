%define	fname		PyOpenGL

Summary:	Python bindings for OpenGL
Name:		python-opengl
Version:	2.0.1.09
Release:	%mkrel 8
License:	BSD
Group:		System/Libraries
URL:		http://pyopengl.sourceforge.net/
# Upstream tarball with OpenGL/Demo/NeHe/lesson43/Test.ttf - a copy of
# Arial Sans Italic, which is not freely licensed - removed. It is
# replaced with a link to DejaVu Sans Oblique later in this spec
# - AdamW 2008/03
Source:		%{fname}-%{version}-fontclean.tar.bz2
BuildRequires:	python-devel, mesaglut-devel swig
BuildRequires:	tcl tcl-devel tk tk-devel
BuildRequires:  xorg-x11-Xvfb xorg-x11-xauth 
Requires:	fonts-ttf-dejavu
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Python bindings for OpenGL

%package doc
Summary: Documentation files for %{name}
Group: Development/Python

%description doc
Documentation files for %{name}

%prep
%setup -n %{fname}-%{version} -q
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

python setup.py install --root=%{buildroot} --compile --optimize=2

kill $(cat /tmp/.X$XDISPLAY-lock)

# Replace non-free font file - AdamW 2008/03
ln -s %{_datadir}/fonts/TTF/dejavu/DejaVuSans-Oblique.ttf %{buildroot}%{py_platsitedir}/OpenGL/Demo/NeHe/lesson43/Test.ttf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{py_platsitedir}/*OpenGL*

%files doc
%defattr(-,root,root)
%doc doc/*

