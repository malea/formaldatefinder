# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    # Use Ubuntu 12.04
    config.vm.box = "hashicorp/precise32"

    # Run bootstrap.sh to install packages and setup
    config.vm.provision :shell, :path => "bootstrap.sh"

    # Forward port 5000
    config.vm.network :forwarded_port, host: 5000, guest: 5000

end
