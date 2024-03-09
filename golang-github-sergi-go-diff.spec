# Run tests in check section
%bcond_without check

# https://github.com/sergi/go-diff
%global goipath		github.com/sergi/go-diff
%global forgeurl	https://github.com/sergi/go-diff
Version:		1.3.1

%gometa

Summary:	Diff, match and patch text in Go
Name:		golang-github-sergi-go-diff

Release:	1
Source0:	https://github.com/sergi/go-diff/archive/v%{version}/go-diff-%{version}.tar.gz
URL:		https://github.com/sergi/go-diff
License:	ASL 2.0 and MIT
Group:		Development/Other
BuildRequires:	compiler(go-compiler)
%if %{with check}
BuildRequires:	golang(github.com/stretchr/testify/assert)
%endif
BuildArch:	noarch

%description
go-diff offers algorithms to perform operations required
for synchronizing plain text:

 *  Compare two texts and return their differences.
 *  Perform fuzzy matching of text.
 *  Apply patches onto text.

#-----------------------------------------------------------------------

%package devel
Summary:	%{summary}
Group:		Development/Other
BuildArch:	noarch

%description devel
%{description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%files devel -f devel.file-list
%license APACHE-LICENSE-2.0 LICENSE
%doc AUTHORS CONTRIBUTORS README.md

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n go-diff-%{version}

%build
%gobuildroot

%install
%goinstall

%check
%if %{with check}
%gochecks
%endif

