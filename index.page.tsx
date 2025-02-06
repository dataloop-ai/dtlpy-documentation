import React from "react";
import styled from "styled-components";
import tutorialsIcon from "./assets/site/icons/tutorials.svg";
import onboardingIcon from "./assets/site/icons/onboarding.svg";
import resourcesIcon from "./assets/site/icons/resources.svg";
import { ArrowRightIcon, Button } from "@redocly/theme";
import { Card } from "@redocly/theme/markdoc/components/Cards/Card";
import { Cards } from "@redocly/theme/markdoc/components/Cards/Cards";

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

export default function HomePage() {
    return (
        <Container>
            <Header>
                <Title>Dataloop Developers Portal</Title>
                <Subtitle>
                    A developer portal for beginners and advanced users
                </Subtitle>
                <Button
                    variant="outlined"
                    size="xlarge"
                    to="/tutorials/getting_started/sdk_overview/chapter"
                >
                    Get started <ArrowRightIcon />
                </Button>
            </Header>
            <Cards>
                <Card title="Tutorials" to="/tutorials" icon={tutorialsIcon}>
                    <h2>Step-by-step guides to get started with Dataloop</h2>
                </Card>
                <Card
                    title="Onboarding"
                    to="/onboarding/onboarding"
                    icon={onboardingIcon}
                >
                    Get up and running with Dataloop platform
                </Card>
                <Card title="Resources" to="/resources" icon={resourcesIcon}>
                    SDKs, APIs and developer tools
                </Card>
            </Cards>
        </Container>
    );
}
