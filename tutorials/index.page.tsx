import React from 'react';
import styled from 'styled-components';
import dataManagementIcon from '../assets/site/icons/data-management.svg';
import annotationsIcon from '../assets/site/icons/annotations.svg';
import recipeOntologyIcon from '../assets/site/icons/recipe-ontology.svg';
import taskWorkflowsIcon from '../assets/site/icons/task-workflows.svg';
import analyticsIcon from '../assets/site/icons/analytics.svg';
import faasIcon from '../assets/site/icons/faas.svg';
import pipelinesIcon from '../assets/site/icons/pipelines.svg';
import modelManagementIcon from '../assets/site/icons/model-management.svg';
import applicationsIcon from '../assets/site/icons/applications.svg';

type CardWithCodeProps = {
  title: string;
  description: string;
  icon: string;
  onClick: () => void;
};

const Container = styled.div`
  padding: 2rem;
`;

const Header = styled.div`
  text-align: center;
  margin-bottom: 3rem;
`;

const Title = styled.h1`
  font-size: 2.5rem;
  margin-bottom: 1rem;
`;

const Subtitle = styled.h2`
  font-size: 1.5rem;
  font-weight: normal;
  margin-bottom: 2rem;
`;

const CardWrapper = styled.div`
  cursor: pointer;
  padding: 16px;
  background-color: var(--layer-color-ontonal);
  border-radius: 8px;
  transition: transform 0.2s, box-shadow 0.2s;
  margin-bottom: 16px;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
`;

const TopRow = styled.div`
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;

  img {
    width: 32px;
    height: 32px;
  }

  h4 {
    margin: 0;
    color: var(--text-color);
    font-size: 20px;
    font-weight: 600;
  }
`;

const Description = styled.p`
  margin: 0;
  color: var(--text-color-secondary);
  font-size: 16px;
  line-height: 24px;
`;

const CardsGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  padding: 1rem;
`;

const DlCard = ({ title, description, icon, onClick }: CardWithCodeProps) => {
  return (
    <CardWrapper onClick={onClick}>
      <TopRow>
        <img src={icon} alt={title} />
        <h4>{title}</h4>
      </TopRow>
      <Description>{description}</Description>
    </CardWrapper>
  );
};

const TutorialsPage = () => (
  <Container>
    <Header>
      <Title>Choose Your AI Adventure! 🎮</Title>
      <Subtitle>
        Explore our interactive guides and level up your Dataloop skills ⚡
      </Subtitle>
    </Header>
    <CardsGrid>
      <DlCard 
        title="Data Management"
        description="Master the art of data wrangling! Learn to organize, version, and manage your AI datasets like a pro"
        icon={dataManagementIcon}
        onClick={() => window.location.href = '/tutorials/data_management'}
      />
      <DlCard 
        title="Annotations"
        description="Turn raw data into AI gold! Discover all the ways to annotate and label your datasets with precision"
        icon={annotationsIcon}
        onClick={() => window.location.href = '/tutorials/annotations'}
      />
      <DlCard 
        title="Recipe and Ontology"
        description="Create the perfect recipe for your AI success! Design powerful ontologies and labeling schemes"
        icon={recipeOntologyIcon}
        onClick={() => window.location.href = '/tutorials/recipe_and_ontology'}
      />
      <DlCard 
        title="Task and Workflows"
        description="Orchestrate your team like a symphony! Master task management and workflow automation"
        icon={taskWorkflowsIcon}
        onClick={() => window.location.href = '/tutorials/task_workflows'}
      />
      <DlCard 
        title="Analytics"
        description="Unlock insights from your data! Dive deep into metrics, trends, and performance analysis"
        icon={analyticsIcon}
        onClick={() => window.location.href = '/tutorials/analytics'}
      />
      <DlCard 
        title="FaaS Applications"
        description="Functions as a Service: Your serverless superpower for scalable AI operations"
        icon={faasIcon}
        onClick={() => window.location.href = '/tutorials/faas_applications'}
      />
      <DlCard 
        title="Pipelines"
        description="Build automated AI workflows that flow like magic! Connect, automate, and orchestrate"
        icon={pipelinesIcon}
        onClick={() => window.location.href = '/tutorials/pipelines'}
      />
      <DlCard 
        title="Model Management"
        description="Train, deploy, and monitor your AI models with style! From experiment to production"
        icon={modelManagementIcon}
        onClick={() => window.location.href = '/tutorials/model_management'}
      />
      <DlCard 
        title="Applications"
        description="Create powerful AI apps that wow! Extend Dataloop with custom applications and integrations"
        icon={applicationsIcon}
        onClick={() => window.location.href = '/tutorials/applications'}
      />
    </CardsGrid>
  </Container>
);

export default TutorialsPage;

