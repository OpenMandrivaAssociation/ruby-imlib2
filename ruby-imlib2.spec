%define rbname imlib2
%define version 0.5.2
%define release %mkrel 1

Summary: Imlib2 bindings for Ruby
Name: ruby-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Other
License: BSD-like
URL: http://ruby-imlib2.rubyforge.org/
Source0: %{rbname}-ruby-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: ruby-devel 
BuildRequires: imlib2-devel

%define ruby_libdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')
%define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

%description
Imlib2 bindings for Ruby.

%prep
%setup -q -n %{rbname}-ruby-%{version}

%build
ruby extconf.rb
make

%install
make install DESTDIR=%{buildroot}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO doc examples
%{ruby_archdir}/%{rbname}.so


