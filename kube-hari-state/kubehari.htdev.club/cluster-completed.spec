apiVersion: kops.k8s.io/v1alpha2
kind: Cluster
metadata:
  creationTimestamp: "2022-06-25T16:22:03Z"
  name: kubehari.htdev.club
spec:
  api:
    dns: {}
  authorization:
    rbac: {}
  channel: stable
  cloudConfig:
    awsEBSCSIDriver:
      enabled: true
      version: v1.5.0
    manageStorageClasses: true
  cloudProvider: aws
  clusterDNSDomain: cluster.local
  configBase: kube-hari-state/kubehari.htdev.club
  configStore: kube-hari-state/kubehari.htdev.club
  containerRuntime: containerd
  containerd:
    logLevel: info
    version: 1.6.4
  dnsZone: kubehari.htdev.club
  docker:
    skipInstall: true
  etcdClusters:
  - backups:
      backupStore: kube-hari-state/kubehari.htdev.club/backups/etcd/main
    cpuRequest: 200m
    etcdMembers:
    - encryptedVolume: true
      instanceGroup: master-ap-south-1a
      name: a
    memoryRequest: 100Mi
    name: main
    version: 3.5.3
  - backups:
      backupStore: kube-hari-state/kubehari.htdev.club/backups/etcd/events
    cpuRequest: 100m
    etcdMembers:
    - encryptedVolume: true
      instanceGroup: master-ap-south-1a
      name: a
    memoryRequest: 100Mi
    name: events
    version: 3.5.3
  externalDns:
    provider: dns-controller
  iam:
    allowContainerRegistry: true
    legacy: false
  keyStore: kube-hari-state/kubehari.htdev.club/pki
  kubeAPIServer:
    allowPrivileged: true
    anonymousAuth: false
    apiAudiences:
    - kubernetes.svc.default
    apiServerCount: 1
    authorizationMode: Node,RBAC
    bindAddress: 0.0.0.0
    cloudProvider: aws
    enableAdmissionPlugins:
    - NamespaceLifecycle
    - LimitRanger
    - ServiceAccount
    - DefaultStorageClass
    - DefaultTolerationSeconds
    - MutatingAdmissionWebhook
    - ValidatingAdmissionWebhook
    - NodeRestriction
    - ResourceQuota
    etcdServers:
    - https://127.0.0.1:4001
    etcdServersOverrides:
    - /events#https://127.0.0.1:4002
    featureGates:
      CSIMigrationAWS: "true"
      InTreePluginAWSUnregister: "true"
    image: k8s.gcr.io/kube-apiserver:v1.23.8
    kubeletPreferredAddressTypes:
    - InternalIP
    - Hostname
    - ExternalIP
    logLevel: 2
    requestheaderAllowedNames:
    - aggregator
    requestheaderExtraHeaderPrefixes:
    - X-Remote-Extra-
    requestheaderGroupHeaders:
    - X-Remote-Group
    requestheaderUsernameHeaders:
    - X-Remote-User
    securePort: 443
    serviceAccountIssuer: https://api.internal.kubehari.htdev.club
    serviceAccountJWKSURI: https://api.internal.kubehari.htdev.club/openid/v1/jwks
    serviceClusterIPRange: 100.64.0.0/13
    storageBackend: etcd3
  kubeControllerManager:
    allocateNodeCIDRs: true
    attachDetachReconcileSyncPeriod: 1m0s
    cloudProvider: aws
    clusterCIDR: 100.96.0.0/11
    clusterName: kubehari.htdev.club
    configureCloudRoutes: true
    enableLeaderMigration: true
    featureGates:
      CSIMigrationAWS: "true"
      InTreePluginAWSUnregister: "true"
    image: k8s.gcr.io/kube-controller-manager:v1.23.8
    leaderElection:
      leaderElect: true
    logLevel: 2
    useServiceAccountCredentials: true
  kubeDNS:
    cacheMaxConcurrent: 150
    cacheMaxSize: 1000
    cpuRequest: 100m
    domain: cluster.local
    memoryLimit: 170Mi
    memoryRequest: 70Mi
    nodeLocalDNS:
      cpuRequest: 25m
      enabled: false
      image: k8s.gcr.io/dns/k8s-dns-node-cache:1.21.3
      memoryRequest: 5Mi
    provider: CoreDNS
    serverIP: 100.64.0.10
  kubeProxy:
    clusterCIDR: 100.96.0.0/11
    cpuRequest: 100m
    image: k8s.gcr.io/kube-proxy:v1.23.8
    logLevel: 2
  kubeScheduler:
    featureGates:
      CSIMigrationAWS: "true"
      InTreePluginAWSUnregister: "true"
    image: k8s.gcr.io/kube-scheduler:v1.23.8
    leaderElection:
      leaderElect: true
    logLevel: 2
  kubelet:
    anonymousAuth: false
    cgroupDriver: systemd
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      CSIMigrationAWS: "true"
      InTreePluginAWSUnregister: "true"
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause:3.6
    podManifestPath: /etc/kubernetes/manifests
    protectKernelDefaults: true
    shutdownGracePeriod: 30s
    shutdownGracePeriodCriticalPods: 10s
  kubernetesApiAccess:
  - 0.0.0.0/0
  - ::/0
  kubernetesVersion: 1.23.8
  masterInternalName: api.internal.kubehari.htdev.club
  masterKubelet:
    anonymousAuth: false
    cgroupDriver: systemd
    cgroupRoot: /
    cloudProvider: aws
    clusterDNS: 100.64.0.10
    clusterDomain: cluster.local
    enableDebuggingHandlers: true
    evictionHard: memory.available<100Mi,nodefs.available<10%,nodefs.inodesFree<5%,imagefs.available<10%,imagefs.inodesFree<5%
    featureGates:
      CSIMigrationAWS: "true"
      InTreePluginAWSUnregister: "true"
    kubeconfigPath: /var/lib/kubelet/kubeconfig
    logLevel: 2
    nonMasqueradeCIDR: 100.64.0.0/10
    podInfraContainerImage: k8s.gcr.io/pause:3.6
    podManifestPath: /etc/kubernetes/manifests
    protectKernelDefaults: true
    registerSchedulable: false
    shutdownGracePeriod: 30s
    shutdownGracePeriodCriticalPods: 10s
  masterPublicName: api.kubehari.htdev.club
  networkCIDR: 172.20.0.0/16
  networking:
    kubenet: {}
  nonMasqueradeCIDR: 100.64.0.0/10
  podCIDR: 100.96.0.0/11
  secretStore: kube-hari-state/kubehari.htdev.club/secrets
  serviceClusterIPRange: 100.64.0.0/13
  sshAccess:
  - 0.0.0.0/0
  - ::/0
  subnets:
  - cidr: 172.20.32.0/19
    name: ap-south-1a
    type: Public
    zone: ap-south-1a
  - cidr: 172.20.64.0/19
    name: ap-south-1b
    type: Public
    zone: ap-south-1b
  topology:
    dns:
      type: Public
    masters: public
    nodes: public
