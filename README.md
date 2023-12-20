# 使用 Ansible 实现滚动更新演示

```sh
cd ansible
ansible-playbook -i inventory.yml rolling_update.yml
```

在更新期间可使用 `locust` 对服务进行小规模的压测以查看效果。
