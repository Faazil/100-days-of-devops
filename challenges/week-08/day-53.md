# Challenge 53: Resolve VolumeMounts Issue in Kubernetes

## 📊 Metadata
- **Day**: 53
- **Week**: 8
- **Day in Week**: 4/7
- **Category**: Kubernetes
- **Difficulty**: ⭐⭐ Intermediate
- **Estimated Time**: 20-30 minutes

---

## 🎯 Challenge Description

We encountered an issue with our Nginx and PHP-FPM setup on the Kubernetes cluster this morning, which halted its functionality. Investigate and rectify the issue:

- The pod name is `nginx-phpfpm` and configmap name is `nginx-config`. Identify and fix the problem.

- Once resolved, copy `/home/thor/index.php` file from the jump host to the `nginx-container` within the nginx document root. After this, you should be able to access the website using Website button on the top bar.

> Note: The kubectl utility on jump_host is configured to operate with the Kubernetes cluster.


## 📋 Prerequisites

> ⚠️ **Important**: This challenge must be completed on **[KodeKloud Engineer](https://kodekloud.com/kodekloud-engineer)**. You'll need to sign up (free) to access the lab environment with pre-configured servers and infrastructure.

**What KodeKloud Provides:**
- ✅ Pre-configured lab environment
- ✅ Kubernetes cluster with kubectl configured
- ✅ Necessary access and permissions
- ✅ Automated validation of your solution

**What You Need to Know:**
- **Command Line Tools**: `kubectl`, `kubectl apply`, `kubectl get`, `kubectl describe`, `kubectl logs`
- **Key Concepts**:
  - Kubernetes resources (Pods, Deployments, Services)
  - YAML manifest structure
  - Resource requests and limits
  - Labels and selectors
- **File Formats**: YAML syntax and structure
- **Environment**: kubectl configured to access Kubernetes cluster

**Foundation from Earlier Challenges:**
- Day 50: Set Resource Limits in Kubernetes Cluster (recommended)
- Day 51: Execute Rolling Updates in Kubernetes (recommended)
- Day 52: Execute Rollback in Kubernetes Cluster (recommended)

**Required Skills:**
- ✅ Write Kubernetes YAML manifests
- ✅ Deploy resources using kubectl
- ✅ Debug pods and containers
- ✅ Understand Kubernetes architecture

---

**🔗 Learn More**: [KodeKloud 100 Days of DevOps](https://kodekloud.com/kodekloud-engineer/100-days-of-devops)

## Steps

1. Let's get the pod yaml config:

    ```sh
    kubectl get pod nginx-phpfpm -o yaml > nginx-phpfpm.yml
    ```

2. Let's fix the yaml file:

    ```sh
    vi nginx-phpfpm.yml
    ```

    > There are two containers: nginx, phpfpm; If we notice carefully, shared-files volume path are not same in both container VolumeMounts. If you failed to find the error, then copy-paste content to AI(chatgpt, claude, copilot, etc) and ask where the issue and fix it. So it will show the issue and solutions as well.

    ```YAML
    apiVersion: v1
    kind: Pod
    metadata:
    annotations:
        kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{},"labels":{"app":"php-app"},"name":"nginx-phpfpm","namespace":"default"},"spec":{"containers":[{"image":"php:7.2-fpm-alpine","name":"php-fpm-container","volumeMounts":[{"mountPath":"/var/www/html","name":"shared-files"}]},{"image":"nginx:latest","name":"nginx-container","volumeMounts":[{"mountPath":"/usr/share/nginx/html","name":"shared-files"},{"mountPath":"/etc/nginx/nginx.conf","name":"nginx-config-volume","subPath":"nginx.conf"}]}],"volumes":[{"emptyDir":{},"name":"shared-files"},{"configMap":{"name":"nginx-config"},"name":"nginx-config-volume"}]}}
    creationTimestamp: "2025-09-16T12:38:30Z"
    labels:
        app: php-app
    name: nginx-phpfpm
    namespace: default
    resourceVersion: "1254"
    uid: 7f3ade52-601d-46ba-801f-a134088963cf
    spec:
    containers:
    - image: php:7.2-fpm-alpine
        imagePullPolicy: IfNotPresent
        name: php-fpm-container
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /var/www/html
        name: shared-files
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-8pvw6
        readOnly: true
    - image: nginx:latest
        imagePullPolicy: Always
        name: nginx-container
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /usr/share/nginx/html
        name: shared-files
        - mountPath: /etc/nginx/nginx.conf
        name: nginx-config-volume
        subPath: nginx.conf
        - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
        name: kube-api-access-8pvw6
        readOnly: true
    dnsPolicy: ClusterFirst
    enableServiceLinks: true
    nodeName: kodekloud-control-plane
    preemptionPolicy: PreemptLowerPriority
    priority: 0
    restartPolicy: Always
    schedulerName: default-scheduler
    securityContext: {}
    serviceAccount: default
    serviceAccountName: default
    terminationGracePeriodSeconds: 30
    tolerations:
    - effect: NoExecute
        key: node.kubernetes.io/not-ready
        operator: Exists
        tolerationSeconds: 300
    - effect: NoExecute
        key: node.kubernetes.io/unreachable
        operator: Exists
        tolerationSeconds: 300
    volumes:
    - emptyDir: {}
        name: shared-files
    - configMap:
        defaultMode: 420
        name: nginx-config
        name: nginx-config-volume
    - name: kube-api-access-8pvw6
        projected:
        defaultMode: 420
        sources:
        - serviceAccountToken:
            expirationSeconds: 3607
            path: token
        - configMap:
            items:
            - key: ca.crt
                path: ca.crt
            name: kube-root-ca.crt
        - downwardAPI:
            items:
            - fieldRef:
                apiVersion: v1
                fieldPath: metadata.namespace
                path: namespace
    status:
    conditions:
    - lastProbeTime: null
        lastTransitionTime: "2025-09-16T12:38:30Z"
        status: "True"
        type: Initialized
    - lastProbeTime: null
        lastTransitionTime: "2025-09-16T12:38:42Z"
        status: "True"
        type: Ready
    - lastProbeTime: null
        lastTransitionTime: "2025-09-16T12:38:42Z"
        status: "True"
        type: ContainersReady
    - lastProbeTime: null
        lastTransitionTime: "2025-09-16T12:38:30Z"
        status: "True"
        type: PodScheduled
    containerStatuses:
    - containerID: containerd://1e1f4de8f73ec6567764229239dcbf6ef98c1e248ad3604ac862e3a6257046e5
        image: docker.io/library/nginx:latest
        imageID: docker.io/library/nginx@sha256:d5f28ef21aabddd098f3dbc21fe5b7a7d7a184720bc07da0b6c9b9820e97f25e
        lastState: {}
        name: nginx-container
        ready: true
        restartCount: 0
        started: true
        state:
        running:
            startedAt: "2025-09-16T12:38:41Z"
    - containerID: containerd://03a0e4d416ea4f9c0b15faab1e126a61d75cbeb2233163aff9b2bc8498784b95
        image: docker.io/library/php:7.2-fpm-alpine
        imageID: docker.io/library/php@sha256:2e2d92415f3fc552e9a62548d1235f852c864fcdc94bcf2905805d92baefc87f
        lastState: {}
        name: php-fpm-container
        ready: true
        restartCount: 0
        started: true
        state:
        running:
            startedAt: "2025-09-16T12:38:34Z"
    hostIP: 172.17.0.2
    phase: Running
    podIP: 10.244.0.5
    podIPs:
    - ip: 10.244.0.5
    qosClass: BestEffort
    startTime: "2025-09-16T12:38:30Z"
    ```

    > Which volume path is the right one? To be confirmed the right mount path let's see the data of `nginx-config` configmap.

    ![shared-path-issue](../screenshots/kubernetes_shared_file_path_issue.png)

3. To see the configmap data:

    ```sh
    kubectl get configmap -o yaml
    ```

    ```YAML
    - apiVersion: v1
    data:
        nginx.conf: |
        events {
        }
        http {
            server {
            listen 8099 default_server;
            listen [::]:8099 default_server;

            # Set nginx to serve files from the shared volume!
            root /var/www/html;
            index  index.html index.htm index.php;
            server_name _;
            location / {
                try_files $uri $uri/ =404;
            }
            location ~ \.php$ {
                include fastcgi_params;
                fastcgi_param REQUEST_METHOD $request_method;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                fastcgi_pass 127.0.0.1:9000;
            }
            }
        }
    kind: ConfigMap
    ```

    > we can see our nginx root directory is: `/var/www/html`. So let's update the mount path of nginx container with this. Once we updated the `nginx-phpfpm.yml`, let's move into the next steps.

4. Let's re-create the pod

    ```sh
    kubectl delete pod nginx-phpfpm
    kubectl apply -f nginx-phpfpm.yml
    ```

5. Now, let's copy `index.php`

    ```sh
    kubectl cp /home/thor/index.php nginx-phpfpm:/var/www/html/index.php -c nginx-container
    ```

6. Test:

    ```sh
    curl localhost:8080
    ```

## Good to Know?

### Volume Troubleshooting

- **Mount Path Mismatch**: Containers must share same mount path
- **ConfigMap Issues**: Verify ConfigMap exists and is correctly named
- **Permission Problems**: Check file system permissions
- **Volume Types**: emptyDir, hostPath, PVC, ConfigMap, Secret

### Multi-Container Pods

- **Shared Volumes**: Containers share volumes within pod
- **Sidecar Pattern**: Helper containers alongside main application
- **Data Sharing**: Share files between containers
- **Log Aggregation**: Collect logs from multiple containers

### ConfigMap Volumes

- **Configuration Files**: Mount config files into containers
- **subPath**: Mount specific files from ConfigMap
- **File Mode**: Set file permissions for mounted files
- **Updates**: ConfigMap changes reflect in mounted volumes

### Debugging Techniques

- **Describe Pod**: `kubectl describe pod` shows events and issues
- **Pod Logs**: `kubectl logs pod-name -c container-name`
- **Exec into Pod**: `kubectl exec -it pod-name -c container -- /bin/sh`
- **Volume Inspection**: Check mount points and file contents

---

## ✅ Verification

After completing the challenge, verify your solution by:

1. **Testing the implementation**
   - Run all commands from the solution
   - Check for any error messages

2. **Validating the results**
   - Ensure all requirements are met
   - Test edge cases if applicable

3. **Clean up (if needed)**
   - Remove temporary files
   - Reset any test configurations

---

## 📚 Learning Notes

### Key Concepts

This challenge covers the following concepts:
- Practical application of Kubernetes skills
- Real-world DevOps scenarios
- Best practices for production environments

### Common Pitfalls

- ⚠️ **Permissions**: Ensure you have the necessary permissions to execute commands
- ⚠️ **Syntax**: Double-check command syntax and flags
- ⚠️ **Environment**: Verify you're working in the correct environment/server

### Best Practices

- ✅ Always verify changes before marking as complete
- ✅ Test your solution in a safe environment first
- ✅ Document any deviations from the standard approach
- ✅ Keep security in mind for all configurations

---

## 🔗 Related Challenges

- **← Previous**: [Day 52 - Execute Rollback in Kubernetes Cluster](./day-52.md)
- **Next →**: [Day 54 - Kubernetes Shared Volumes](../week-08/day-54.md)

### Similar Challenges (Kubernetes)
- [Day 48 - Deploy Pods in Kubernetes Cluster](../week-07/day-48.md)
- [Day 49 - Deploy Applications with Kubernetes Deployments](../week-07/day-49.md)
- [Day 50 - Set Resource Limits in Kubernetes Cluster](../week-08/day-50.md)

---

## 📖 Additional Resources

- [KodeKloud Official Documentation](https://kodekloud.com)
- [Official Technology Documentation](#)
- [Community Discussions](#)

---

## 🎓 Knowledge Check

After completing this challenge, you should be able to:
- [ ] Understand the problem statement clearly
- [ ] Implement the solution independently
- [ ] Verify the solution works correctly
- [ ] Explain the concepts to others
- [ ] Apply these skills to similar problems

---

**Challenge Source**: KodeKloud 100 Days of DevOps
**Difficulty**: {get_difficulty_emoji(day)}
**Category**: {task_info['category']}

---

**Track your progress**: After completing this challenge, mark it as done:
```bash
python3 ../../tools/progress.py --complete {day}
```

