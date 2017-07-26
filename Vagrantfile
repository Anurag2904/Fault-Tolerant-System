
Vagrant.configure("2") do |config|
 
  config.vm.box = "ubuntu/xenial64"
  config.vm.boot_timeout = 600
  
  config.vm.provision "file", source: "./anurag_cloud.pem", destination: "~/.ssh/anurag_cloud.pem"
  
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook_local.yml"
    ansible.verbose = true
    ansible.install = true  # installs ansible (and hence python on VM)
    ansible.limit = "all"
    ansible.inventory_path = "hosts"  # inventory file
  end
 
  
end
