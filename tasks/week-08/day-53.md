# Day 53: Resolve VolumeMounts Issue in Kubernetes

## Task Overview

Configure resource constraints for Kubernetes pods to prevent performance degradation. Define CPU and memory limits to ensure fair resource distribution and stable cluster operations.

**Resource Configuration:**
- Pod creation with resource specifications
- Memory requests and limits (Mi units)
- CPU requests and limits (millicores)
- Prevent resource contention across workloads

**Lab:** [KodeKloud Engineer Platform](https://engineer.kodekloud.com/practice)

---

## Solution Steps

**Step 1:** Verify the resource was created and check its status.

```sh
kubectl get pod nginx-phpfpm -o yaml > nginx-phpfpm.yml
```

**Step 2:** Execute the command to complete this step.

```sh
vi nginx-phpfpm.yml
```

**Step 3:** Execute the command to complete this step.

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

**Step 4:** Verify the resource was created and check its status.

```sh
kubectl get configmap -o yaml
```

**Step 5:** Execute the command to complete this step.

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

**Step 6:** Apply the configuration to the Kubernetes cluster.

```sh
kubectl delete pod nginx-phpfpm
    kubectl apply -f nginx-phpfpm.yml
```

**Step 7:** Execute the command to complete this step.

```sh
kubectl cp /home/thor/index.php nginx-phpfpm:/var/www/html/index.php -c nginx-container
```

**Step 8:** Execute the command to complete this step.

```sh
curl localhost:8080
```

---

## Validation

Test your solution using KodeKloud's automated validation.

---

[← Day 52](day-52.md) | [Day 54 →](day-54.md)

**Source:** [100 Days of DevOps](https://engineer.kodekloud.com/practice/100-days-of-devops)
