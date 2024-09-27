%global module rich
%global mod %(m=%{module}; echo ${m:0:1})

Summary:	A Python library for rich text and beautiful formatting in the terminal
Name:		python-%{module}
Version:	13.8.1
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/Textualize/rich
#Source0::		https://github.com/Textualize/rich/v%{version}/%{module}-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/%{mod}/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
# tests
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(attrs)

BuildArch:	noarch

%description
Rich is a Python library for rich text and beautiful formatting in the terminal.

The Rich API makes it easy to add color and style to terminal output. Rich can
alsorender pretty tables, progress bars, markdown, syntax highlighted source
code, tracebacks, and more — out of the box.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-*-info/

#-----------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

