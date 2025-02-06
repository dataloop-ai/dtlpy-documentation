import React from 'react';
import styled from 'styled-components';
import { Card } from '@redocly/theme/markdoc/components/Cards/Card';
import { Cards } from '@redocly/theme/markdoc/components/Cards/Cards';

import dataManagementIcon from '../assets/site/icons/data-management.svg';
import annotationsIcon from '../assets/site/icons/annotations.svg';
import recipeOntologyIcon from '../assets/site/icons/recipe-ontology.svg';
import taskWorkflowsIcon from '../assets/site/icons/task-workflows.svg';
import analyticsIcon from '../assets/site/icons/analytics.svg';
import faasIcon from '../assets/site/icons/faas.svg';
import pipelinesIcon from '../assets/site/icons/pipelines.svg';
import modelManagementIcon from '../assets/site/icons/model-management.svg';
import applicationsIcon from '../assets/site/icons/applications.svg';

const Container = styled.div`
  padding: 2rem;
`;

const TutorialsPage = () => (
  <Container>
    <Cards>
      <Card title="Data Management" to="data_management.md" icon={dataManagementIcon}>
        Tutorials for data management
      </Card>
      <Card title="Annotations" to="annotations.md" icon={annotationsIcon}>
        Tutorials for creating all types of annotations for file types
      </Card>
      <Card title="Recipe and Ontology" to="recipe_and_ontology.md" icon={recipeOntologyIcon}>
        Tutorials for managing ontologies, labels, and recipes
      </Card>
      <Card title="Task and Workflows" to="task_workflows.md" icon={taskWorkflowsIcon}>
        Tutorials for workforce management
      </Card>
      <Card title="Analytics" to="analytics.md" icon={analyticsIcon}>
        Extract and Analyze Analytics
      </Card>
      <Card title="FaaS Tutorial" to="faas.md" icon={faasIcon}>
        Tutorials for FaaS
      </Card>
      <Card title="Pipelines" to="pipelines.md" icon={pipelinesIcon}>
        Tutorials for creating pipelines with the SDK
      </Card>
      <Card title="Model Management" to="model_management.md" icon={modelManagementIcon}>
        Tutorials for creating and managing ML model
      </Card>
      <Card title="Applications" to="applications.md" icon={applicationsIcon}>
        Developing and working with the Dataloop Applications
      </Card>
    </Cards>
  </Container>
);

export default TutorialsPage;

