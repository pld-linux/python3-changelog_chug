# Conditional build:
%bcond_without	tests	# unit tests

%define		module	changelog_chug
Summary:	A parser for project Change Log documents
Name:		python3-%{module}
Version:	0.0.3
Release:	1
License:	AGPL v3+
Group:		Libraries/Python
Source0:	https://pypi.debian.net/changelog-chug/changelog_chug-%{version}.tar.gz
# Source0-md5:	4ccd595cfa9e929bfa04b7e64de3663c
URL:		https://pypi.org/project/changelog-chug/
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-semver
%if %{with tests}
BuildRequires:	python3-testscenarios
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# replace with other requires if defined in setup.py
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A parser for project Change Log documents.

%prep
%setup -q -n changelog_chug-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
PYTHONPATH="$PWD/build-3/lib" \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{py3_sitescriptdir}/chug
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
