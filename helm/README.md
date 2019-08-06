# <img src="./logo.png" width=60/> Demo testbed of Federator.ai Operator
**It is based on Federator.ai Operator codes [federatorai-operator](https://github.com/containers-ai/federatorai-operator)**

**Federator.ai Operator** is an Operator that manages **Federator.ai** components for an OpenShift cluster. Once installed, the Federator.ai Operator provides the following features:
- **Create/Clean up**: Launch **Federator.ai** components using the Operator.
- **Easy Configuration**: Easily configure data source of Prometheus and enable/disable add-on components, such as GUI, and predictive autoscaling.
- **Pod Scaling Recommendation/Autoscaling**: Use provided CRD to setup target pods and desired policies for scaling recommendation and autoscaling.

> **Note:** **Federator.ai** requires a Prometheus datasource to get historical metrics of pods and nodes. When launching **Federator.ai** components, Prometheus connection settings need to be provided.

## Federator.ai

**Federator.ai** is the brain of resource orchestration for kubernetes. We use machine learning technology to provide intelligence that foresees future resource usage of your Kubernetes cluster across multiple layers. Federator.ai recommends the right sizes of containers and the right number of replications. It also elastically manages pod scaling and scheduling of your containerized applications. The overall benefit is cost reduction up to 50% and higher service quality, such as fewer OOM issues. For more information, visit [github.com/containers-ai/alameda](https://github.com/containers-ai/alameda)

## Prerequisites
- Kubernetes v1.14.1+
- Prometheus

## Installing
```
helm install --namespace federatorai federatorai-demo
```

## Installing with the release name `my-name`:
```
helm install --name `my-name` --namespace federatorai federatorai-demo
```

## To uninstall/delete the `my-name` deployment:
```
helm ls --all
helm delete `my-name`
```

