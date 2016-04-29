#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-atomic
Version  : 1.1.99
Release  : 8
URL      : https://rubygems.org/downloads/atomic-1.1.99.gem
Source0  : https://rubygems.org/downloads/atomic-1.1.99.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rubygem-atomic-lib
BuildRequires : ruby
BuildRequires : ruby-dev
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rdoc

%description
# Ruby Atomic
[![Gem Version](https://badge.fury.io/rb/atomic.svg)](http://badge.fury.io/rb/atomic) [![Build Status](https://travis-ci.org/ruby-concurrency/atomic.svg?branch=master)](https://travis-ci.org/ruby-concurrency/atomic) [![Code Climate](https://codeclimate.com/github/ruby-concurrency/atomic.svg)](https://codeclimate.com/github/ruby-concurrency/atomic) [![Dependency Status](https://gemnasium.com/ruby-concurrency/atomic.svg)](https://gemnasium.com/ruby-concurrency/atomic) [![License](https://img.shields.io/badge/license-Apache-green.svg)](http://opensource.org/licenses/Apache-2.0) [![Gitter chat](http://img.shields.io/badge/gitter-join%20chat%20%E2%86%92-brightgreen.svg)](https://gitter.im/ruby-concurrency/concurrent-ruby)

%package lib
Summary: lib components for the rubygem-atomic package.
Group: Libraries

%description lib
lib components for the rubygem-atomic package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n atomic-1.1.99
gem spec %{SOURCE0} -l --ruby > rubygem-atomic.gemspec

%build
gem build rubygem-atomic.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
atomic-1.1.99.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/atomic-1.1.99
ruby -v -I.:lib:test test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/atomic-1.1.99.gem
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/atomic-1.1.99/gem.build_complete
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/atomic-1.1.99/gem_make.out
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/atomic-1.1.99/mkmf.log
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/.coveralls.yml
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/README.md
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/atomic.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/examples/atomic_example.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/examples/bench_atomic.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/examples/bench_atomic_1.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/examples/graph_atomic_bench.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/AtomicReferenceService.java
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/Makefile
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/atomic_reference.c
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/atomic_reference.o
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/extconf.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/org/jruby/ext/atomic/AtomicReferenceLibrary.java
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/concurrent_update_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/delegated_update.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/direct_update.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/fallback.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/jruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/numeric_cas_wrapper.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/rbx.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic/ruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/test/test_atomic.rb
/usr/lib64/ruby/gems/2.3.0/specifications/atomic-1.1.99.gemspec

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/extensions/x86_64-linux/2.3.0/atomic-1.1.99/atomic_reference.so
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/ext/atomic_reference.so
/usr/lib64/ruby/gems/2.3.0/gems/atomic-1.1.99/lib/atomic_reference.so
