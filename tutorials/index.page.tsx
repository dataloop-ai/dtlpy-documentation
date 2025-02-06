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
      <Card title="Data Management" to="/tutorials/data_management" icon={dataManagementIcon}>
        Tutorials for data management
      </Card>
      <Card title="Annotations" to="/tutorials/annotations" icon={annotationsIcon}>
        Tutorials for creating all types of annotations for file types
      </Card>
      <Card title="Recipe and Ontology" to="/tutorials/recipe_and_ontology" icon={recipeOntologyIcon}>
        Tutorials for managing ontologies, labels, and recipes
      </Card>
      <Card title="Task and Workflows" to="/tutorials/task_workflows" icon={taskWorkflowsIcon}>
        Tutorials for workforce management
      </Card>
      <Card title="Analytics" to="/tutorials/analytics" icon={analyticsIcon}>
        Extract and Analyze Analytics
      </Card>
      <Card title="FaaS Tutorial" to="/tutorials/faas" icon={faasIcon}>
        Tutorials for FaaS
      </Card>
      <Card title="Pipelines" to="/tutorials/pipelines" icon={pipelinesIcon}>
        Tutorials for creating pipelines with the SDK
      </Card>
      <Card title="Model Management" to="/tutorials/model_management" icon={modelManagementIcon}>
        Tutorials for creating and managing ML model
      </Card>
      <Card title="Applications" to="/tutorials/applications" icon={applicationsIcon}>
        Developing and working with the Dataloop Applications
      </Card>
    </Cards>
  </Container>
);

export default TutorialsPage;

